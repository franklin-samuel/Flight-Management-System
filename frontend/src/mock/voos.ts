import type { Voo } from '../types/models';

export const mockVoos: Voo[] = [
  {
    id: 1,
    companhiaId: 1,
    numero_voo: 'AZ101',
    origem: 'São Paulo (GRU)',
    destino: 'Rio de Janeiro (GIG)',
    aeronave: 'Airbus A320',
    capacidade: 180,
    passageiros: 170,
    tripulacao: 6,
  },
  {
    id: 2,
    companhiaId: 1,
    numero_voo: 'AZ202',
    origem: 'São Paulo (GRU)',
    destino: 'Salvador (SSA)',
    aeronave: 'Boeing 737',
    capacidade: 160,
    passageiros: 120,
    tripulacao: 5,
  }
];
