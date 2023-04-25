import APIService from "./APIService";


class ResearcherService extends APIService {
    getAllResearchers() {
        return this.get('/get_researchers')
    }
    addResearcher(arr: any[]) {
        const data = {
            Name: arr[0],
            Email: arr[1],
            ResearcherEmail: arr[2],
        }
        return this.post('/add_assistant_researcher', data)
    }
    updateResearcher(arr: any) {
        const data = {
            Name: arr[0],
            Email: arr[1],
            ResearcherEmail: arr[2],
        }
        return this.put('/update_assistant_researcher', data)
    }
    deleteResearcher(arr: any) {
        const data = {
            Email: arr[1],
            ResearcherEmail: arr[2]
        }
        return this.delete('/del_assistant_researcher', data)
    }
    getFilteredResearchers(data: any) {
        return this.get('/get_assistant_researchers_filtered', data)
    }
    getColumn(params: any) {
        return this.get('/get_assistant_researcher_column', params);
    }
}

export default new ResearcherService();