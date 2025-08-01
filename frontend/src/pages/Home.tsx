import { Card, CardContent, CardHeader } from "../components/ui/Card";
import { Building2, Plane, Users, UserCheck } from 'lucide-react'
import { useCompanhia } from "../context/companhiaContext";

export default function Home() {
  
  const { companhia } = useCompanhia()

  const stats = [
    {
      title: 'Companhias Aéreas',
      value: 2,
      icon: Building2,
      color: 'text-blue-600 bg-blue-100'
    },
    {
      title: 'Voos Cadastrados',
      value: 8,
      icon: Plane,
      color: 'text-green-600 bg-green-100'
    },
    {
      title: 'Passageiros',
      value: 50,
      icon: Users,
      color: 'text-purple-600 bg-purple-100'
    },
    {
      title: 'Funcionários',
      value: 43,
      icon: UserCheck,
      color: 'text-orange-600 bg-orange-100'
    }
  ];

  // Dados mockados de voos por companhia
  const voosPorCompanhia = [
    { companhia: "Gol", voos: 4 },
    { companhia: "Latam", voos: 3 },
    { companhia: "Azul", voos: 1 },
  ];

  const maxVoos = Math.max(...voosPorCompanhia.map(v => v.voos));

  return (
    <div className="space-y-8">
      <div className="flex items-center justify-between">
        <h1 className="text-3xl font-bold text-gray-900">Dashboard</h1>
        <div className="text-sm text-gray-500">
          Sistema de Gerenciamento de Voos
        </div>
      </div>

      {/* Cards de Estatísticas */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
        {stats.map((stat, index) => (
          <Card key={index}>
            <CardContent className="flex items-center space-x-4">
              <div className={`p-3 rounded-full ${stat.color}`}>
                <stat.icon className="h-6 w-6" />
              </div>
              <div>
                <p className="text-sm font-medium text-gray-600">{stat.title}</p>
                <p className="text-2xl font-bold text-gray-900">{stat.value}</p>
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Gráfico de Voos por Companhia (mockado) */}
      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Voos por Companhia</h2>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            {voosPorCompanhia.map((item, index) => (
              <div key={index} className="flex items-center justify-between">
                <span className="text-sm font-medium text-gray-700">{item.companhia}</span>
                <div className="flex items-center space-x-2">
                  <div className="w-32 bg-gray-200 rounded-full h-2">
                    <div
                      className="bg-blue-600 h-2 rounded-full"
                      style={{
                        width: `${Math.max(10, (item.voos / maxVoos) * 100)}%`
                      }}
                    ></div>
                  </div>
                  <span className="text-sm font-bold text-gray-900">{item.voos}</span>
                </div>
              </div>
            ))}
          </div>
        </CardContent>
      </Card>

      {/* Informações do Sistema */}
      <Card>
        <CardHeader>
          <h2 className="text-xl font-semibold text-gray-900">Sobre o Sistema</h2>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div>
              <h3 className="font-semibold text-gray-700 mb-2">Funcionalidades</h3>
              <ul className="text-sm text-gray-600 space-y-1">
                <li>• Gerenciamento de companhias aéreas</li>
                <li>• Cadastro e controle de voos</li>
                <li>• Gestão de passageiros e bagagens</li>
                <li>• Controle de funcionários e tripulação</li>
                <li>• Relatórios de auditoria</li>
              </ul>
            </div>
            <div>
              <h3 className="font-semibold text-gray-700 mb-2">Tecnologias</h3>
              <ul className="text-sm text-gray-600 space-y-1">
                <li>• Backend: Python + Flask + SQLAlchemy</li>
                <li>• Frontend: React + TypeScript</li>
                <li>• Banco: SQLite</li>
                <li>• Testes: PyTest</li>
                <li>• Relatórios: ReportLab (PDF)</li>
              </ul>
            </div>
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
