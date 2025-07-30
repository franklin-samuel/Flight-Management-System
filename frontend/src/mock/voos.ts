import type { Voo } from '../types/models';

export const mockVoos: Voo[] = [
  {
    id: 1,
    companhiaId: 1,
    numero_voo: 'AZ101',
    origem: 'São Paulo (GRU)',
    destino: 'Rio de Janeiro (GIG)',
    aeronave: {
      id: 1,
      modelo: 'Airbus A320',
      capacidade: 180
    },
    capacidade: 180,
    passageiros: [],
    tripulacao: [],
  },
  {
    id: 2,
    companhiaId: 2,
    numero_voo: 'JJ202',
    origem: 'Brasília (BSB)',
    destino: 'Salvador (SSA)',
    aeronave: {
      id: 2,
      modelo: 'Boeing 737',
      capacidade: 160
    },
    capacidade: 160,
    passageiros: [],
    tripulacao: [],
  }
];
