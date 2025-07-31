import { createContext, useContext, useState } from 'react';
import { type ReactNode } from 'react';
import { type Companhia } from '../types/models';
// import axios from 'axios';

interface CompanhiaContextType {
  companhia: Companhia | null;
  carregarCompanhia: (id: number) => void;
  carregando: boolean;
}

const CompanhiaContext = createContext<CompanhiaContextType>({
  companhia: null,
  carregarCompanhia: () => {},
  carregando: false,
});

export const useCompanhia = () => useContext(CompanhiaContext);

export const CompanhiaProvider = ({ children }: { children: ReactNode }) => {
  const [companhia, setCompanhia] = useState<Companhia | null>(null);
  const [carregando, setCarregando] = useState(false);

  const carregarCompanhia = (id: number) => {
    setCarregando(true);

    // Simula um GET /companhias/:id
    setTimeout(() => {
      const mock: Companhia = {
        id,
        nome: 'TAM Airlines',
        voos: [
          {
            id: 1,
            numero_voo: 'AZ101',
            origem: 'São Paulo',
            destino: 'Rio de Janeiro',
            aeronave: {
              id: 1,
              modelo: 'Airbus A320',
              capacidade: 180,
            },
            tripulacao: [
              {
                id: 1,
                nome: 'Capitão João',
                cpf: '00000000000',
                cargo: 'Piloto',
                matricula: 'ABC123',
              },
            ],
            passageiros: [
              {
                id: 1,
                nome: 'Carlos Silva',
                cpf: '13708316410',
                bagagens: [
                  { id: 1, peso: 12.5, descricao: 'Mala de mão' },
                  { id: 2, peso: 23, descricao: 'Bagagem despachada' },
                ],
              },
              {
                id: 2,
                nome: 'Ana Paula',
                cpf: '78949972472',
                bagagens: [
                  { id: 3, peso: 18, descricao: 'Mochila' },
                ],
              },
            ],
          },
        ],
      };

      setCompanhia(mock);
      setCarregando(false);
    }, 500);

    // No futuro:
    // axios.get(`/companhias/${id}`).then(response => {
    //   setCompanhia(response.data);
    //   setCarregando(false);
    // });
  };

  return (
    <CompanhiaContext.Provider value={{ companhia, carregarCompanhia, carregando }}>
      {children}
    </CompanhiaContext.Provider>
  );
};
