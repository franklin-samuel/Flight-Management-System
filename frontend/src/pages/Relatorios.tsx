import React, { useState } from 'react';
import { Card, CardHeader, CardContent } from '../components/ui/Card';
import { Button } from '../components/ui/Button';
import { FileBarChart, Download, Calendar, AlertTriangle } from 'lucide-react';

export const Relatorios: React.FC = () => {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');

  const mockDownloadPDF = async () => {
    setLoading(true);
    setError('');

    try {
      await new Promise((resolve) => setTimeout(resolve, 1000)); // simula geração do PDF
        //Exemplo não funcional, API será responsável pela geração de formulários
      const blob = new Blob(
        [`
        RELATÓRIO DE AUDITORIA (SIMULADO)
        ----------------------------------
        Todos os voos foram verificados com base nas regras de capacidade e tripulação mínima.
        Nenhuma inconformidade encontrada.
      `],
        { type: 'application/pdf' }
      );

      const url = window.URL.createObjectURL(blob);
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'relatorio_auditoria.pdf');
      document.body.appendChild(link);
      link.click();
      link.remove();
      window.URL.revokeObjectURL(url);
    } catch (err) {
      setError('Erro ao simular download do relatório');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const relatorios = [
    {
      id: 'auditoria',
      titulo: 'Relatório de Auditoria de Voos',
      descricao:
        'Relatório completo com status de conformidade de todos os voos cadastrados, incluindo verificação de capacidade e tripulação.',
      icon: FileBarChart,
      action: mockDownloadPDF,
      color: 'text-blue-600 bg-blue-100',
    },
  ];

  return (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-gray-900">Relatórios do Sistema</h1>
        <div className="flex items-center space-x-2 text-sm text-gray-500">
          <Calendar className="h-4 w-4" />
          <span>Última atualização: {new Date().toLocaleDateString('pt-BR')}</span>
        </div>
      </div>

      {/* Informações sobre Relatórios */}
      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Sobre os Relatórios</h2>
        </CardHeader>
        <CardContent>
          <div className="flex items-start space-x-3">
            <AlertTriangle className="h-5 w-5 text-amber-500 mt-0.5" />
            <div className="text-sm text-gray-600">
              <p>Os relatórios são gerados em tempo real com base nos dados atuais do sistema.</p>
              <p className="mt-1">
                <strong>Relatório de Auditoria:</strong> Verifica se todos os voos estão em conformidade com as regras de capacidade e tripulação mínima.
              </p>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Lista de Relatórios */}
      <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
        {relatorios.map((relatorio) => (
          <Card key={relatorio.id}>
            <CardContent className="p-6">
              <div className="flex items-start space-x-4">
                <div className={`p-3 rounded-full ${relatorio.color}`}>
                  <relatorio.icon className="h-6 w-6" />
                </div>
                <div className="flex-1 min-w-0">
                  <h3 className="text-lg font-semibold text-gray-900 mb-2">
                    {relatorio.titulo}
                  </h3>
                  <p className="text-sm text-gray-600 mb-4">
                    {relatorio.descricao}
                  </p>

                  {error && (
                    <div className="mb-4 p-3 bg-red-50 border border-red-200 rounded-md">
                      <div className="text-red-600 text-sm">{error}</div>
                    </div>
                  )}

                  <Button
                    onClick={relatorio.action}
                    disabled={loading}
                    icon={Download}
                    variant="primary"
                    size="sm"
                  >
                    {loading ? 'Gerando...' : 'Baixar PDF'}
                  </Button>
                </div>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Instruções */}
      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Como Usar</h2>
        </CardHeader>
        <CardContent>
          <div className="space-y-3 text-sm text-gray-600">
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-xs font-semibold">1</div>
              <p>Clique no botão "Baixar PDF" do relatório desejado</p>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-xs font-semibold">2</div>
              <p>Aguarde a geração do arquivo (pode levar alguns segundos)</p>
            </div>
            <div className="flex items-start space-x-3">
              <div className="w-6 h-6 bg-blue-100 text-blue-600 rounded-full flex items-center justify-center text-xs font-semibold">3</div>
              <p>O arquivo será baixado automaticamente para seu computador</p>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
};
