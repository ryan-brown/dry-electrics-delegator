import moment from "moment"
import * as d3 from "d3"

const drawChart = () => {
  const timeConverter = (unixTimestamp) => {
    const a = new Date(unixTimestamp);
    const year = `${a.getFullYear()}`.padStart(4, '0');
    const month = `${a.getMonth()+1}`.padStart(2, '0');
    const date = `${a.getDate()}`.padStart(2, '0');
    const hours = `${a.getHours()}`.padStart(2, '0');
    const min = `${a.getMinutes()}`.padStart(2, '0');
    const time = `${year}-${month}-${date}T${hours}:${min}`;
    return time;
  }

  const pointMouseOver = (pnt, d, i) => {
    svg.append("rect")
      .attr("id", "idrect"+i)
      .attr("x", xScale(d[3]) - 70)
      .attr("y", yScale(d[0]) - 10)
      .attr("width", 200)
      .attr("height", 20)
      .attr("fill", "black")
      .attr("fill-opacity", 0.5)
      .text(() => `${d[0]}% @ ${d[2].substr(0,10)} ${d[2].substr(11,8)}`);

    svg.append("text")
      .attr("id", "idtext"+i)
      .attr("x", xScale(d[3]) - 65)
      .attr("y", yScale(d[0]) + 5)
      .attr("fill", "white")
      .text(() => `${d[0]}% @ ${d[2].substr(0,10)} ${d[2].substr(11,8)}`);

    svg.append("line")
      .attr("id", "lineX")
      .attr("x1", margin.left + xScale(d[3]))
      .attr("y1", margin.top+graphHeight)
      .attr("x2", margin.left +xScale(d[3]))
      .attr("y2", margin.top+graphHeight-yScale(100-d[0]))
      .attr("stroke-width", 1)
      .attr("stroke-dasharray", "3, 3")
      .attr("stroke", "black");

    svg.append("line")
      .attr("id", "lineY")
      .attr("x1", margin.left)
      .attr("y1", margin.top+graphHeight-yScale(100-d[0]))
      .attr("x2", margin.left+xScale(d[3]))
      .attr("y2", margin.top+graphHeight-yScale(100-d[0]))
      .attr("stroke-width", 1)
      .attr("stroke-dasharray", "3, 3")
      .attr("stroke", "black");

    d3.select(pnt)
      .attr("stroke-width", "1")
      .attr("stroke", "#000000")
      .attr("r", 6)
  }

  const pointMouseOut = (pnt, d, i) => {
    d3.select(pnt)
      .attr("stroke", "none")
      .attr("r", 3)

    d3.select("#lineX").remove()
    d3.select("#lineY").remove()
    d3.select("#idrect"+i).remove()
    d3.select("#idtext"+i).remove()
  }

  const addCircles = (data) => {
    const selection = graph.selectAll("circle").data(data)
      .attr("cx", (d) => { return xScale(d[3]) })
      .attr("cy", (d) => { return yScale(d[0]) })
      .attr("r", 3)
      .attr("fill", (d) => { return getPointColor(d[0]) });
    selection.enter()
      .append("circle")
      .attr("cx", (d) => { return xScale(d[3]) })
      .attr("cy", (d) => { return yScale(d[0]) })
      .attr("r", 3)
      .attr("fill", (d) => { return getPointColor(d[0]) })
      .on("mouseover", function(d, i) {pointMouseOver(this, d, i)})
      .on("mouseout", function(d, i) {pointMouseOut(this, d, i)})
    selection.exit().remove();
  }

  const updateChart = () => {
    const startTime = moment(document.getElementById("start-time").value).valueOf();
    const endTime = moment(document.getElementById("end-time").value).valueOf();

    history.replaceState(undefined, undefined, `#${startTime},${endTime}`);

    xScale.domain([startTime, endTime]);
    xAxisCall = d3.axisBottom(xScale).tickSize(-graphHeight);
    xAxis.call(xAxisCall);

    let newData = data.filter(d => d[3] <= endTime && d[3] >= startTime);

    addCircles(newData);
  }

  document.body.onload = () => {
    document.getElementById('chart-svg').addEventListener('mouseenter', () => {
      document.documentElement.style.overflow = "hidden";
      document.body.style.overflow = "auto";
    });

    document.getElementById('chart-svg').addEventListener('mouseleave', () => {
      document.documentElement.style.overflow = "initial";
      document.body.style.overflow = "initial";
    });
  }

  // Shamelessly stolen from lodash and then slightly modified
  const throttle = (func, wait, options) => {
    let timeout, context, args, result;
    let previous = 0;
    if (!options) options = {};

    const later = function() {
      previous = options.leading === false ? 0 : Date.now();
      timeout = null;
      result = func.apply(context, args);
      if (!timeout) context = args = null;
    };

    const throttled = function() {
      const now = Date.now();
      if (!previous && options.leading === false) previous = now;
      const remaining = wait - (now - previous);
      context = this;
      args = arguments;
      if (remaining <= 0 || remaining > wait) {
          if (timeout) {
            clearTimeout(timeout);
            timeout = null;
          }
          previous = now;
          result = func.apply(context, args);
          if (!timeout) context = args = null;
        } else if (!timeout && options.trailing !== false) {
          timeout = setTimeout(later, remaining);
        }
      return result;
    };

    throttled.cancel = function() {
      clearTimeout(timeout);
      previous = 0;
      timeout = context = args = null;
    };

    return throttled;
  };

  // Throttle to every 16 ms, ~60fps
  //window.addEventListener('wheel', throttle((event) => {
  window.addEventListener('wheel', throttle((event) => {
    window.requestAnimationFrame(() => {
      if (document.documentElement.style.overflow !== "hidden") return;

      let startTime = parseInt(moment(document.getElementById("start-time").value).valueOf());
      let endTime = parseInt(moment(document.getElementById("end-time").value).valueOf());

      // Scale scroll interval relative to time interval
      const interval = (endTime - startTime) / 500;

      let delta;

      if (event.wheelDelta){
        delta = event.wheelDelta;
      } else {
        delta = -1 * event.deltaY;
      }

      startTime += delta*interval;
      endTime += delta*interval;

      setDateDirectly(timeConverter(startTime), timeConverter(endTime));
      updateChart();
    });
  }, 16));

  const toHex = (num) => (num < 16) ? `0${num.toString(16)}` : num.toString(16)

  const getPointColor = (percentage) => {
    let red, green;
    if (percentage <= 50) {
      red = 255;
      green = Math.round(255 * percentage * 2 / 100);
    }
    else {
      red = Math.round(255 * (1 - (percentage - 50) * 2 / 100));
      green = 255;
    }

    return `#${toHex(red)}${toHex(green)}00`;
  }

  const addZero = (num) => (num < 10) ? `0${num}` : num;

  const formatDate = (dt) => dt.replace(" ", "T").substr(0,16);

  const setDateDirectly = (startTime, endTime) =>
  {
    document.getElementById("start-time").value = startTime;
    document.getElementById("end-time").value = endTime;
  }

  const setDates = (startTime, endTime) => {
    document.getElementById("start-time").value = formatDate(startTime);
    document.getElementById("end-time").value = formatDate(endTime);
  }

  const initializeSVG = (width, height) =>
    d3.select("div#inner-chart").append("svg").attr("width", width).attr("height", height).attr("id", 'chart-svg')

  const initializeTimeWindow = (data) => {
    const hash = window.location.hash;

    if (hash === "") {
      return [data[0][2], data[data.length - 1][2]]
    } else {
      const fromHash = hash.substr(1).split(",").map(e => (new Date(parseInt(e))))
      return fromHash.map(d => {
        const datePrefix = `${d.getFullYear()}-${addZero(d.getMonth()+1)}-${addZero(d.getDate())}`;
        const dateTime = `${addZero(d.getHours())}:${addZero(d.getMinutes())}`;

        return `${datePrefix} ${dateTime}`;
      })
    }
  }

  let data = window.gon.data.map(d => [ d['percentage'], d['charging'], d['updated_at'], moment(d['updated_at']).valueOf()])
  const firstTime = data[0][2];
  const lastTime = data[data.length - 1][2];

  const [initialFirstTime, initialLastTime] = initializeTimeWindow(data);

  setDates(initialFirstTime, initialLastTime);

  const svg = initializeSVG(800, 600);

  const margin = {top: 25, right: 25, bottom: 25, left: 25};
  const graphWidth = +svg.attr("width") - margin.left - margin.right;
  const graphHeight = +svg.attr("height") - margin.top - margin.bottom;

  const graph = svg.append("g").attr("transform", `translate(${margin.left},${margin.top})`);

  const xScale = d3.scaleTime()
      .domain([moment(initialFirstTime).valueOf(), moment(initialLastTime).valueOf()])
      .range([0, graphWidth]);

  const yScale = d3.scaleLinear()
      .domain([0, 100])
      .range([graphHeight, 0]);

  let xAxisCall = d3.axisBottom(xScale).tickSize(-graphHeight);
  const xAxis = graph.append("g")
      .attr("transform", `translate(0, ${graphHeight})`)
      .call(xAxisCall);

  let yAxisCall = d3.axisLeft(yScale).tickSize(-graphWidth)
  const yAxis = graph.append("g")
      .call(yAxisCall);

  const lineGenerator = d3.line()
    .x((d) => xScale(d[3]))
    .y((d) => yScale(d[0]));


  updateChart();

  document.getElementById("start-time").addEventListener("change", updateChart);
  document.getElementById("end-time").addEventListener("change", updateChart);

  document.getElementById("all-button").addEventListener("click", () => {
    setDates(firstTime, lastTime);
    updateChart();
  });

  document.getElementById("today-button").addEventListener("click", () => {
    const today = moment().format("YYYY-MM-DD")
    const startTime = `${today}T09:00`;
    const endTime = `${today}T19:00`;

    setDates(startTime, endTime);
    updateChart();
  });

  document.getElementById("week-button").addEventListener("click", () => {
    const sunday = moment().day(0).startOf('day').format("YYYY-MM-DD")+"T00:00"
    const saturday = moment().day(6).startOf('day').format("YYYY-MM-DD")+"T00:00"

    setDates(sunday, saturday);
    updateChart();
  });
}

export default drawChart;