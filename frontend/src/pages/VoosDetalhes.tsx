// src/pages/VooDetalhes.tsx
import React from 'react';
import { useParams } from 'react-router-dom';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Users, Luggage, UserCheck, Plane } from 'lucide-react';

interface Passageiro {
  id: number;
  nome: string;
  bagagens: number;
}

const passageirosMock: Passageiro[] = [
  { id: 1, nome: 'Carlos Silva', bagagens: 2 },
  { id: 2, nome: 'Ana Paula', bagagens: 1 },
  { id: 3, nome: 'João Pedro', bagagens: 3 },
];

export const VooDetalhes: React.FC = () => {
  const { id } = useParams(); // ID do voo

  // Em um caso real, aqui você buscaria os dados do voo com esse ID
  const voo = {
    id,
    numero_voo: 'AZ101',
    origem: 'São Paulo (GRU)',
    destino: 'Rio de Janeiro (GIG)',
    aeronave: 'Airbus A320',
    capacidade: 180,
    passageiros: 170,
    tripulacao: 6,
  };

  return (
    <div className="space-y-6">
      <h1 className="text-3xl font-bold text-gray-900">Detalhes do Voo {voo.numero_voo}</h1>

      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Informações do Voo</h2>
        </CardHeader>
        <CardContent className="space-y-2">
          <div className="flex items-center space-x-2">
            <Plane className="w-5 h-5 text-blue-600" />
            <span className="text-sm text-gray-700">{voo.origem} → {voo.destino}</span>
          </div>
          <div className="flex items-center space-x-2">
            <Users className="w-5 h-5 text-blue-600" />
            <span className="text-sm text-gray-700">{voo.passageiros}/{voo.capacidade} passageiros</span>
          </div>
          <div className="flex items-center space-x-2">
            <UserCheck className="w-5 h-5 text-blue-600" />
            <span className="text-sm text-gray-700">{voo.tripulacao} tripulantes</span>
          </div>
        </CardContent>
      </Card>

      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Passageiros</h2>
        </CardHeader>
        <CardContent className="space-y-4">
          {passageirosMock.map((p) => (
            <div key={p.id} className="flex items-center justify-between p-3 border rounded-md">
              <span className="text-gray-800">{p.nome}</span>
              <div className="flex items-center space-x-2 text-sm text-gray-600">
                <Luggage className="w-4 h-4" />
                <span>{p.bagagens} bagagens</span>
              </div>
            </div>
          ))}
        </CardContent>
      </Card>
    </div>
  );
};
