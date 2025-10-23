export const View = (() => {
  let onTeamSelect;

  return {
    init({ handleTeamSelect }) {
      onTeamSelect = handleTeamSelect;
    },

    renderDropdown(teams) {
      const dropdown = document.getElementById('teamsDropdown');
      dropdown.innerHTML = '';
      teams.forEach(team => {
        const option = document.createElement('option');
        option.textContent = team;
        option.value = team;
        dropdown.appendChild(option);
      });
    },

    renderTeamInfo(team) {
      document.getElementById('infoDiv').innerHTML = `
        <h1>Info about ${team.strTeam}</h1>
        <h3>${team.strDescriptionEN}</h3>
      `;
      document.getElementById('BadgeDiv').innerHTML = `<img src="${team.strBadge}" alt="Badge">`;
      document.getElementById('BannerDiv').innerHTML = `<img src="${team.strBanner}" alt="Banner">`;
      this.applyTeamColors(team);
    },

    renderWeather(details) {
      const tempF = (details.air_temperature * 9/5 + 32).toFixed(2);
      const windMph = (details.wind_speed / 0.447).toFixed(2);
      const humidity = details.relative_humidity.toFixed(1);

      document.getElementById('weatherDiv').innerHTML = `
        <div class="columns">
          <div class="column is-one-third" id="temperature"><h1>Temperature</h1><h3>${tempF} °F</h3></div>
          <div class="column is-one-third" id="wind_speed"><h1>Wind Speed</h1><h3>${windMph} mph</h3></div>
          <div class="column is-one-third" id="humidity"><h1>Humidity</h1><h3>${humidity} %</h3></div>
        </div>
      `;
    },

    renderRecentSearches(recent) {
  const list = document.getElementById('recentList');
  list.innerHTML = '';

  recent.forEach(team => {
    const li = document.createElement('li');
    li.textContent = team;
    li.className = 'column is-one-third has-text-centered'; 
    li.style.cursor = 'pointer';
    li.onclick = () => onTeamSelect(team);
    list.appendChild(li);
  });
}
,

    applyTeamColors(team) {
      const primary = team.strColour1 || "#ffffff";
      const secondary = team.strColour2 || "#000000";
      document.body.style.backgroundColor = primary;
      document.body.style.color = secondary;
      document.querySelectorAll(".box").forEach(box => {
        box.style.backgroundColor = secondary;
        box.style.color = primary;
      });
        const dropdown = document.getElementById("teamsDropdown");
        dropdown.style.backgroundColor = secondary;
        dropdown.style.color = primary;
    }
  };
})();
