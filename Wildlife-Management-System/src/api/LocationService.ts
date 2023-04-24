import APIService from "./APIService";


class LocationService extends APIService {
    getAllLocations() {
        return this.get('/get_locations')
    }
    addLocation(arr: any[]) {
        const data = {
            Latitude: arr[0],
            Longitude: arr[1],
            LocationName: arr[2],
            LocationType: arr[3],
            Country: arr[4],
            Area: arr[5],
            Climate: arr[6],
            Elevation: arr[7]
        }
        return this.post('/add_location', data)
    }
    updateLocation(arr: any) {
        const data = {
            Latitude: arr[0],
            Longitude: arr[1],
            LocationName: arr[2],
            LocationType: arr[3],
            Country: arr[4],
            Area: arr[5],
            Climate: arr[6],
            Elevation: arr[7]
        }
        console.log("NEW DATA", data)
        return this.put('/update_location', data)
    }
    getFilteredLocation(data: any) {
        return this.get('/get_locations_filtered', data)
    }
}

export default new LocationService();