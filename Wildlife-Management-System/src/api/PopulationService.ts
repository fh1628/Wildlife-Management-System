import APIService from "./APIService";


class PopulationService extends APIService {
    getAllPopulations() {
        return this.get('/get_populations')
    }
    getFilteredPopulations(params: any) {
        return this.get('/get_populations_filtered', params)
    }

    getColumn(params: any) {
        return this.get('/get_population_column', params);
    }

    addPopulation(arr: any[]) {
        const data = {
            PopulationID: arr[0],
            Size: arr[1],
            Trend: arr[2],
            GrowthRate: arr[3],
            Density: arr[4],
            HabitatName: arr[5],
            SpeciesScientificName: arr[6]
        }
        console.log(data)
        return this.post('/add_population', data)
    }
    updatePopulation(arr: any) {
        const data = {
            PopulationID: arr[0],
            Size: arr[1],
            Trend: arr[2],
            GrowthRate: arr[3],
            Density: arr[4],
            HabitatName: arr[5],
            SpeciesScientificName: arr[6]
        }
        console.log(data)
        return this.put('/update_population', data)
    }

    deletePopulation(arr: any) {
        const data = {
            PopulationID: arr[0],
        }
        return this.delete('/del_population', data)
    }

    sortPopulation(params: any) {
        return this.get('/sort_population', params)
    }
}

export default new PopulationService();