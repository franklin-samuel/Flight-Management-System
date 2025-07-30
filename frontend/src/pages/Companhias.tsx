import React, { useState, useEffect, useRef } from 'react';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { Building2, Plus } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

interface Companhia {
  id: number;
  nome: string;
  total_voos: number;
}

export const Companhias: React.FC = () => {
  const [companhias, setCompanhias] = useState<Companhia[]>([]);
  const [loading, setLoading] = useState(true);
  const [showForm, setShowForm] = useState(false);
  const [novaCompanhia, setNovaCompanhia] = useState('');
  const [error, setError] = useState('');

  const navigate = useNavigate()

  const idCounter = useRef(4);

  const mockCompanhias = useRef<Companhia[]>([
    { id: 1, nome: 'TAM Airlines', total_voos: 12 },
    { id: 2, nome: 'GOL Linhas Aéreas', total_voos: 8 },
    { id: 3, nome: 'Azul', total_voos: 15 },
  ]);

  useEffect(() => {
    fetchCompanhiasMock();
  }, []);

  const fetchCompanhiasMock = () => {
    setLoading(true);
    setTimeout(() => {
      setCompanhias(mockCompanhias.current);
      setLoading(false);
    }, 600);
  };

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    if (novaCompanhia.trim().length < 3) {
      setError('Nome da companhia deve ter ao menos 3 caracteres');
      return;
    }

    const nova: Companhia = {
      id: idCounter.current++,
      nome: novaCompanhia.trim(),
      total_voos: 0,
    };

    mockCompanhias.current = [...mockCompanhias.current, nova];
    setNovaCompanhia('');
    setShowForm(false);
    fetchCompanhiasMock();
  };

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-gray-900">Companhias Aéreas</h1>
        <Button
          onClick={() => setShowForm(!showForm)}
          icon={Plus}
          variant="primary"
        >
          Nova Companhia
        </Button>
      </div>

      {/* Formulário */}
      {showForm && (
        <Card>
          <CardHeader>
            <h2 className="text-xl font-semibold text-gray-900">Nova Companhia Aérea</h2>
          </CardHeader>
          <CardContent>
            <form onSubmit={handleSubmit} className="space-y-4">
              <div>
                <label className="block text-sm font-medium text-gray-700 mb-2">
                  Nome da Companhia
                </label>
                <input
                  type="text"
                  value={novaCompanhia}
                  onChange={(e) => setNovaCompanhia(e.target.value)}
                  className="w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
                  placeholder="Ex: LATAM"
                  required
                />
              </div>

              {error && (
                <div className="text-red-600 text-sm">{error}</div>
              )}

              <div className="flex space-x-3">
                <Button variant="primary">
                  Criar Companhia
                </Button>
                <Button
                  variant="secondary"
                  onClick={() => {
                    setShowForm(false);
                    setError('');
                    setNovaCompanhia('');
                  }}
                >
                  Cancelar
                </Button>
              </div>
            </form>
          </CardContent>
        </Card>
      )}

      {/* Lista de Companhias */}
      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">
            Companhias Cadastradas ({companhias.length})
          </h2>
        </CardHeader>
        <CardContent>
          {loading ? (
            <div className="text-center py-8 text-gray-600">Carregando...</div>
          ) : companhias.length === 0 ? (
            <div className="text-center py-8 text-gray-600">
              <Building2 className="mx-auto h-12 w-12 text-gray-400 mb-4" />
              <p>Nenhuma companhia cadastrada.</p>
              <p className="text-sm">Clique em "Nova Companhia" para começar.</p>
            </div>
          ) : (
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
              {companhias.map((companhia) => (
                <div
                  key={companhia.id}
                  onClick={() => navigate(`/companhias/${companhia.id}`)}
                  className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow"
                >
                  <div className="flex items-center space-x-3">
                    <div className="p-2 bg-blue-100 rounded-full">
                      <Building2 className="h-5 w-5 text-blue-600" />
                    </div>
                    <div className="flex-1 min-w-0">
                      <h3 className="text-lg font-semibold text-gray-900 truncate">
                        {companhia.nome}
                      </h3>
                      <p className="text-sm text-gray-600">
                        {companhia.total_voos} voos cadastrados
                      </p>
                    </div>
                  </div>
                </div>
              ))}
            </div>
          )}
        </CardContent>
      </Card>
    </div>
  );
};
