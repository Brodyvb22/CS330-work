import { Model } from './model.js';
import { View } from './view.js';

window.onload = () => {
  View.init({ handleTeamSelect });

  Model.subscribe({
    teamList: View.renderDropdown,
    teamInfo: team => {
      View.renderTeamInfo(team);
      Model.fetchCoordinates(team.strLocation, team.strStadium);
      Model.updateRecentSearches(team.strTeam);
    },
    coordinates: coords => Model.fetchWeather(coords.lat, coords.lon),
    weather: View.renderWeather,
    recentUpdate: recent => View.renderRecentSearches(recent)
  });

  Model.fetchTeams();
  View.renderRecentSearches(Model.getRecentSearches());

  document.querySelector('form').addEventListener('submit', e => {
    e.preventDefault();
    const team = document.getElementById('teamsDropdown').value;
    if (team) handleTeamSelect(team);
  });

  function handleTeamSelect(teamName) {
    Model.fetchTeamInfo(teamName);
  }
};
