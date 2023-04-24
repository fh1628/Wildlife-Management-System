import APIService from "./APIService";


class LocationService extends APIService {
    getAllLocations() {
        return this.get('/get_locations')
    }
    addLocation(arr: any[]) {
        const data = {
            latitude: arr[0],
            longitude: arr[1],
            location_name: arr[2],
            location_type: arr[3],
            location_country: arr[4],
            location_area: arr[5],
            location_climate: arr[6],
            location_elevation: arr[7]
        }
        return this.post('/add_location', data)
    }
    updateLocation(arr: any) {
        const data = {
            latitude: arr[0],
            longitude: arr[1],
            location_name: arr[2],
            location_type: arr[3],
            location_country: arr[4],
            location_area: arr[5],
            location_climate: arr[6],
            location_elevation: arr[7]
        }
        console.log("NEW DATA", data)
        return this.put('/update_location', data)
    }
}

export default new LocationService();