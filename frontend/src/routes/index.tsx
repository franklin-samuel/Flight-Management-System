import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Navbar } from '../components/layout/NavBar';
import Home from '../pages/Home';
import { Voos } from '../pages/Voos';
import Auditoria from '../pages/Auditoria';
import { Funcionarios } from '../pages/Funcionarios';
import { Companhias } from '../pages/Companhias';
import { Relatorios } from '../pages/Relatorios';

export default function RoutesApp() {
    return (
        <BrowserRouter>
            <div className='min-h-screen bg-gray-50'>
                <Navbar />
                <main className='container mx-auto px-4 py-8'>
                    <Routes>
                        <Route path="/" element={<Home />} />
                        <Route path="/Voos" element={<Voos />} />
                        <Route path="/Funcionarios" element={<Funcionarios />}/>
                        <Route path="/Auditoria" element={<Auditoria />} />
                        <Route path="/Companhias" element={<Companhias />} />
                        <Route path="/Relatorios" element={<Relatorios />} />
                    </Routes>
                </main>
            </div>
        </BrowserRouter>
    )
}