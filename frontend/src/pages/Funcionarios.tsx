import React, { useEffect, useState, useRef } from "react";
import { Card, CardContent, CardHeader } from "../components/ui/Card";
import { Button } from "../components/ui/Button";
import { UserCheck, Plus, Briefcase } from "lucide-react";

interface Funcionario {
    id: number,
    nome: string,
    cpf: string,
    cargo: string,
    matricula: string
}

export const Funcionarios: React.FC = () => {
    const [funcionarios, setFuncionarios] = useState<Funcionario[]>([])
    const [loading, setLoading] = useState(true)
    const [showForm, setShowForm] = useState(false)
    const [novoFuncionario, setNovoFuncionario] = useState({
        nome: '',
        cpf: '',
        cargo: '',
        matricula: '',
    })
    const [error, setError] = useState('')

    // Dados mockados, trocar por vindos da API depois
    const nextId = useRef(4);
    const mockStorage = useRef<Funcionario[]>([
        { id: 1, nome: 'Ana Beatriz', cpf: '13708316410', cargo: 'Comissária', matricula: 'CM101'  },
        { id: 2, nome: 'Carlos Silva', cpf: '00949972456', cargo: 'Piloto', matricula: 'FN001'  },
        { id: 3, nome: 'João Oliveira', cpf: '39336972472', cargo: 'Mecânico', matricula: 'ME202'  }
    ])

    useEffect(() => {
        fetchFuncionariosMock();
    }, [])

    const fetchFuncionariosMock = () => {
        setLoading(true);
        setTimeout(() => {
            setFuncionarios(mockStorage.current);
            setLoading(false)
        }, 800) //simula chamada de API
    }

    const addFuncionarioMock = (funcionario: Omit<Funcionario, 'id'>) => {
        const novo = { ...funcionario, id: nextId.current++ };
        mockStorage.current.push(novo);
        fetchFuncionariosMock();
    }

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        setError('')

        const { nome, cpf, cargo, matricula } = novoFuncionario;

        if (nome.trim().length < 2) return setError('Nome deve haver ao menos 2 caracteres');
        if (cpf.trim().length !== 11) return setError('CPF deve ter 11 dígitos');
        if (cargo.trim().length < 2) return setError('Cargo deve haver ao menos 3 caracteres');
        if (matricula.trim().length < 3) return setError('Matrícula deve haver ao menos 3 caracteres') ;

        addFuncionarioMock(novoFuncionario);
        setNovoFuncionario({ nome: '', cpf: '', cargo: '', matricula: '' })
        setShowForm(false)
    };

    const getCargoBadgeColor = (cargo: string) => {
        const c = cargo.toLocaleLowerCase();
        if (c.includes('piloto')) return 'bg-blue-100 text-blue-800';
        if (c.includes('comissário') || c.includes('comissária')) return 'bg-green-100 text-green-800';
        if (c.includes('mecânico')) return 'bg-orange-100 text-orange-800';
        return 'bg-gray-100 text-gray-800';
    };

    return (
        <div className="space-y-6">
            <div className="flex items-center justify-between">
                <h1 className="text-3x1 font-bold text-gray-900">Gerenciamento de Funcionários</h1>
                <Button onClick={() => setShowForm(!showForm)} icon={Plus} variant="primary">
                    Novo Funcionário
                </Button>
            </div>

            {showForm && (
                <Card>
                    <CardHeader>
                        <h2 className="text-x1 font-semibold text-gray-900">Novo Funcionário</h2>
                    </CardHeader>
                    <CardContent>
                        <form onSubmit={handleSubmit} className="space-y-4">
                            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                                {['nome', 'CPF', 'cargo', 'matricula'].map((field) => (
                                    <div key={field}>
                                        <label className="block text-sm font-medium text-gray-700 mb-2">
                                            {field.charAt(0).toUpperCase() + field.slice(1)}
                                        </label>
                                        <input 
                                        type="text" 
                                        value={(novoFuncionario as any)[field]}
                                        onChange={(e) =>
                                            setNovoFuncionario({ ...novoFuncionario, [field]: e.target.value })
                                        }
                                        className="w-full px-3 py-2 border border-gray-300"
                                        placeholder={`Digite ${field}`}
                                        required
                                        />
                                    </div>
                                ))}
                            </div>

                            {error && <div className="text-red-600 text-sm">{error}</div>}

                            <div className="flex space-x-3">
                                <Button variant="primary">
                                    Criar Funcionário
                                </Button>
                                <Button
                                    variant="secondary"
                                    onClick={() => {
                                        setShowForm(false);
                                        setError('');
                                        setNovoFuncionario({ nome: '', cpf: '', cargo: '', matricula: '' })
                                    }}
                                >
                                    Cancelar
                                </Button>
                            </div>
                        </form>
                    </CardContent>
                </Card>
            )}

            <Card>
                <CardHeader>
                    <h2 className="text-x1 font-semibold text-gray-900">Funcionários Cadastrados ({funcionarios.length})</h2>
                </CardHeader>
                <CardContent>
                    {loading ? (
                        <div className="text-center py-8 text-gray-600">Carregando...</div>
                    ): funcionarios.length === 0 ? (
                        <div className="text-center py-8 text-gray-600">
                            <UserCheck className="mx-auto h-12 w-12 text-gray-400 mb-4" />
                            <p>Nenhum funcionário cadastrado.</p>
                            <p className="text-sm">Clique em "Novo Funcionário" para começar.</p>
                        </div>
                    ) : (
                       <div className="space-y-3">
                            {funcionarios.map((funcionario) => (
                                <div key={funcionario.id} className="border border-gray-200 rounded-lg p-4 hover:shadow-md transition-shadow">
                                    <div className="flex items-center justify-between">
                                        <div className="p-2 bg-orange-100 rounded-full">
                                            <UserCheck className="h-5 w-5 text-orange-600" />
                                        </div>
                                        <div>
                                            <h3 className="text-lg font-semibold text-gray-900">
                                                {funcionario.nome}
                                            </h3>
                                            <p className="text-sm text-gray-600">
                                                CPF: {funcionario.cpf} • Matrícula: {funcionario.matricula}
                                            </p>
                                        </div>
                                    </div>
                                    <div className="flex items-center space-x-3">
                                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${getCargoBadgeColor(funcionario.cargo)}`}>
                                            {funcionario.cargo}
                                        </span>
                                        <Briefcase className="h-4 w-4 text-gray-400" />
                                    </div>
                                </div>
                            ))}
                       </div> 
                    )}
                </CardContent>
            </Card>
        </div>
    );
}

