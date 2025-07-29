import { BrowserRouter, Routes, Route } from 'react-router-dom';
import Home from '../pages/Home';
import Voos from '../pages/Voos';
import Auditoria from '../pages/Auditoria';

export default function RoutesApp() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<Home />}/>
                <Route path="/Voos" element={<Voos />}/>
                <Route path="/Auditoria" element={<Auditoria />}/>
            </Routes>
        </BrowserRouter>
    )
}