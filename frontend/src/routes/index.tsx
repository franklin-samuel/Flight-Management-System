import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { CompanhiaProvider } from '../context/companhiaContext';
import { Navbar } from '../components/layout/NavBar';
import Home from '../pages/Home';
import { Voos } from '../pages/Voos';
import Auditoria from '../pages/Auditoria';
import { Funcionarios } from '../pages/Funcionarios';
import { Companhias } from '../pages/Companhias';
import { CompanhiaDetalhes } from '../pages/CompanhiaDetalhes';
import { Relatorios } from '../pages/Relatorios';
import { VooDetalhes } from '../pages/VoosDetalhes';
import Passageiro from '../pages/PassageiroDetalhes';

export default function RoutesApp() {
    return (
        <BrowserRouter>
            <div className='min-h-screen bg-gray-50'>
                <Navbar />
                <main className='container mx-auto px-4 py-8'>
                    <CompanhiaProvider>
                        <Routes>
                            <Route path="/" element={<Home />} />
                            <Route path="/Voos" element={<Voos />} />
                            <Route path="/voos/:id" element={<VooDetalhes />} />
                            <Route path="passageiro/:id" element={<Passageiro />} />
                            <Route path="/Funcionarios" element={<Funcionarios />}/>
                            <Route path="/Auditoria" element={<Auditoria />} />
                            <Route path="/Companhias" element={<Companhias />} />
                            <Route path="/companhias/:id" element={<CompanhiaDetalhes />} />
                            <Route path="/Relatorios" element={<Relatorios />} />
                        </Routes>
                    </CompanhiaProvider>
                </main>
            </div>
        </BrowserRouter>
    )
}