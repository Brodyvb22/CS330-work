export const Model = (() => {
  let onTeamList, onTeamInfo, onCoordinates, onWeather, onRecentUpdate;

  return {
    // Subscription registration
    subscribe({ teamList, teamInfo, coordinates, weather, recentUpdate }) {
      onTeamList = teamList;
      onTeamInfo = teamInfo;
      onCoordinates = coordinates;
      onWeather = weather;
      onRecentUpdate = recentUpdate;
    },

    async fetchTeams() {
      const res = await fetch('./teams.json');
      const data = await res.json();
      onTeamList?.(data);
    },

    async fetchTeamInfo(teamName) {
      const url = `https://www.thesportsdb.com/api/v1/json/123/searchteams.php?t=${encodeURIComponent(teamName)}`;
      const res = await fetch(url);
      const data = await res.json();
      const team = data.teams?.[0];
      if (team) onTeamInfo?.(team);
    },

    async fetchCoordinates(location, stadium) {
      //const locWords = location ? location.replace(/,/g, '').split(' ') : [];
      const fieldWords = stadium.split(' ');
      const query = [...fieldWords].join('+');
      const url = `https://nominatim.openstreetmap.org/search?addressdetails=1&q=${query}&format=jsonv2&limit=1`;
      const res = await fetch(url);
      const [coords] = await res.json();
      if (coords) onCoordinates?.(coords);
    },

    async fetchWeather(lat, lon) {
      const url = `https://api.met.no/weatherapi/locationforecast/2.0/compact?lat=${lat}&lon=${lon}`;
      const res = await fetch(url);
      const data = await res.json();
      const details = data.properties.timeseries[0].data.instant.details;
      onWeather?.(details);
    },

    updateRecentSearches(teamName) {
      let recent = JSON.parse(localStorage.getItem('recentTeams')) || [];
      recent = [teamName, ...recent.filter(t => t !== teamName)].slice(0, 3);
      localStorage.setItem('recentTeams', JSON.stringify(recent));
      onRecentUpdate?.(recent);
    },

    getRecentSearches() {
      return JSON.parse(localStorage.getItem('recentTeams')) || [];
    }
  };
})();
