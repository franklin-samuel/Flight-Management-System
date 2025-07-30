export interface Companhia {
  id: number;
  nome: string;
  total_voos: number;
}

export interface Voo {
  id: number;
  companhiaId: number;
  numero_voo: string;
  origem: string;
  destino: string;
  aeronave: string;
  capacidade: number;
  passageiros: number;
  tripulacao: number;
}

export interface Passageiro {
  id: number;
  vooId: number;
  nome: string;
  idade: number;
}

export interface Bagagem {
  id: number;
  passageiroId: number;
  peso: number; // em kg
  descricao: string;
}
