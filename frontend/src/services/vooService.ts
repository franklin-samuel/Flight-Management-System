import { voosMock } from "../mock/voos";

const usarMock = true   

export const getVoos = async () => {
    if (usarMock) {
        return voosMock
    }
}

//Nesse arquivo onde vamos fazer as requisições para API e obter os dados.