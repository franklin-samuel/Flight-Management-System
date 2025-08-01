export interface Companhia {
  id: number;
  nome: string;
  voos: Voo[]
}

export interface Aeronave {
  id: number;
  modelo: string;
  capacidade: number;
}

export interface Voo {
  id: number;
  numero_voo: string;
  origem: string;
  destino: string;
  aeronave: Aeronave;
  passageiros: Passageiro[];
  tripulacao: Funcionario[];
}

export interface Funcionario {
    id: number,
    nome: string,
    cpf: string,
    cargo: string,
    matricula: string
}


export interface Passageiro {
  id: number;
  nome: string;
  cpf: string;
  bagagens: Bagagem[];
}

export interface Bagagem {
  id: number;
  peso: number; 
  descricao: string;
}


