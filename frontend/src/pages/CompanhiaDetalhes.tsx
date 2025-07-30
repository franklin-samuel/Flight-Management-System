import React, { useEffect, useState } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Plane, Users, UserCheck, ArrowLeft, Plus } from 'lucide-react';
import { mockVoos } from '../mock/voos';
import { type Voo } from '../types/models';

export const CompanhiaDetalhes: React.FC = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const companhiaId = Number(id);

  const [voos, setVoos] = useState<Voo[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const carregarVoos = () => {
      setLoading(true);
      setTimeout(() => {
        const voosDaCompanhia = mockVoos.filter((voo) => voo.companhiaId === companhiaId);
        setVoos(voosDaCompanhia);
        setLoading(false);
      }, 500);
    };

    carregarVoos();
  }, [companhiaId]);

  const getOcupacaoStatus = (passageiros: number, capacidade: number) => {
    const percentual = (passageiros / capacidade) * 100;
    if (percentual >= 90) return { color: 'bg-red-500', status: 'Lotado' };
    if (percentual >= 70) return { color: 'bg-yellow-500', status: 'Cheio' };
    return { color: 'bg-green-500', status: 'Disponível' };
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <div className="flex items-center space-x-3">
          <Button
            onClick={() => navigate('/')}
            icon={ArrowLeft}
            variant="secondary"
          >
            Voltar
          </Button>
          <h1 className="text-3xl font-bold text-gray-900">
            Detalhes da Companhia
          </h1>
        </div>
        <Button
          icon={Plus}
          variant="primary"
          onClick={() => alert('Função de adicionar voo ainda não implementada')}
        >
          Novo Voo
        </Button>
      </div>

      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Voos da Companhia</h2>
        </CardHeader>
        <CardContent>
          {loading ? (
            <div className="text-center py-8 text-gray-600">Carregando voos...</div>
          ) : voos.length === 0 ? (
            <div className="text-center py-8 text-gray-600">
              <Plane className="mx-auto h-12 w-12 text-gray-400 mb-4" />
              <p>Nenhum voo cadastrado.</p>
              <p className="text-sm">Clique em "Novo Voo" para adicionar um novo.</p>
            </div>
          ) : (
            <div className="space-y-4">
              {voos.map((voo) => {
                const ocupacao = getOcupacaoStatus(voo.passageiros, voo.capacidade);
                return (
                  <div
                    key={voo.id}
                    className="border border-gray-200 rounded-lg p-6 hover:shadow-md transition-shadow cursor-pointer"
                    onClick={() => navigate(`/voos/${voo.id}`)}
                  >
                    <div className="flex items-center justify-between">
                      <div className="flex items-center space-x-4">
                        <div className="p-3 bg-blue-100 rounded-full">
                          <Plane className="h-6 w-6 text-blue-600" />
                        </div>
                        <div>
                          <h3 className="text-lg font-semibold text-gray-900">
                            Voo {voo.numero_voo}
                          </h3>
                          <p className="text-gray-600">
                            {voo.origem} → {voo.destino}
                          </p>
                          <p className="text-sm text-gray-500">
                            Aeronave: {voo.aeronave}
                          </p>
                        </div>
                      </div>

                      <div className="flex items-center space-x-6">
                        <div className="flex items-center space-x-2">
                          <div className={`w-3 h-3 rounded-full ${ocupacao.color}`}></div>
                          <span className="text-sm font-medium text-gray-700">
                            {ocupacao.status}
                          </span>
                        </div>
                        <div className="flex items-center space-x-2 text-gray-600">
                          <Users className="h-4 w-4" />
                          <span className="text-sm">
                            {voo.passageiros}/{voo.capacidade}
                          </span>
                        </div>
                        <div className="flex items-center space-x-2 text-gray-600">
                          <UserCheck className="h-4 w-4" />
                          <span className="text-sm">{voo.tripulacao} tripulantes</span>
                        </div>
                      </div>
                    </div>

                    <div className="mt-4">
                      <div className="flex items-center justify-between text-xs text-gray-500 mb-1">
                        <span>Ocupação</span>
                        <span>{Math.round((voo.passageiros / voo.capacidade) * 100)}%</span>
                      </div>
                      <div className="w-full bg-gray-200 rounded-full h-2">
                        <div
                          className={`h-2 rounded-full ${ocupacao.color}`}
                          style={{
                            width: `${(voo.passageiros / voo.capacidade) * 100}%`
                          }}
                        ></div>
                      </div>
                    </div>
                  </div>
                );
              })}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};
