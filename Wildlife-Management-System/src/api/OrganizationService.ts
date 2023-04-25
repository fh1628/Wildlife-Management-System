import APIService from "./APIService";


class OrganizationService extends APIService {
    getAllOrganizations() {
        return this.get('/get_organization')
    }

    getColumn(params: any) {
        return this.get('/get_organization_column', params);
    }

    addOrganization(arr: any[]) {
        const data = {
            ContactEmail: arr[0],
            Name: arr[1],
            Mission: arr[2],
            Website: arr[3],
        }
        return this.post('/add_organization', data)
    }
    updateOrganization(arr: any) {
        const data = {
            ContactEmail: arr[0],
            Name: arr[1],
            Mission: arr[2],
            Website: arr[3],
        }
        return this.put('/update_organization', data)
        }

    deleteOrganization(arr: any) {
        const data = {
            ContactEmail: arr[0],
        }
        return this.delete('/del_organization', data)
    }
}

export default new OrganizationService();