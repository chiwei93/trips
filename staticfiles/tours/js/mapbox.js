mapboxgl.accessToken =
  'pk.eyJ1IjoiY2hpd2VpOTMiLCJhIjoiY2txYjY4YTJqMGpubTJvb3Z3ajc0eGZhbSJ9.XuqSTQT5vg8NnsJGK_XkVA';

const map = new mapboxgl.Map({
  container: 'map',
  style: 'mapbox://styles/chiwei93/ckqbzlx8d19g018o1bpzkrysx',
});

const locations = JSON.parse(
  document.getElementById('mapbox_coords').textContent
);

const locationsArr = locations.map(location => {
  return {
    coords: [location.lng, location.lat],
    name: location.name,
  };
});

const bounds = new mapboxgl.LngLatBounds();

locationsArr.forEach(location => {
  new mapboxgl.Marker().setLngLat(location.coords).addTo(map);

  bounds.extend(location.coords);
});

map.fitBounds(bounds, {
  padding: {
    top: 50,
    bottom: 50,
    left: 50,
    right: 50,
  },
});
