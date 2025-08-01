import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Plane, Building2, Users, UserCheck, FileBarChart, Home } from 'lucide-react';

export const Navbar: React.FC = () => {
  const location = useLocation();
  
  const isActive = (path: string) => location.pathname === path;
  
  const navItems = [
    { path: '/', label: 'Dashboard', icon: Home },
    { path: '/companhias', label: 'Companhias', icon: Building2 },
    { path: '/voos', label: 'Voos', icon: Plane },
    { path: '/passageiros', label: 'Passageiros', icon: Users },
    { path: '/funcionarios', label: 'Funcionários', icon: UserCheck },
    { path: '/relatorios', label: 'Relatórios', icon: FileBarChart },
  ];
  
  return (
    <nav className="bg-white shadow-lg border-b border-gray-200">
      <div className="container mx-auto px-4">
        <div className="flex items-center justify-between h-16">
          <div className="flex items-center space-x-2">
            <Plane className="h-8 w-8 text-blue-600" />
            <h1 className="text-xl font-bold text-gray-900">FlyFlask</h1>
          </div>
          
          <div className="flex space-x-8">
            {navItems.map(({ path, label, icon: Icon }) => (
              <Link
                key={path}
                to={path}
                className={`flex items-center space-x-2 px-3 py-2 rounded-md text-sm font-medium transition-colors duration-200 ${
                  isActive(path)
                    ? 'bg-blue-100 text-blue-700'
                    : 'text-gray-600 hover:text-gray-900 hover:bg-gray-100'
                }`}
              >
                <Icon className="h-4 w-4" />
                <span>{label}</span>
              </Link>
            ))}
          </div>
        </div>
      </div>
    </nav>
  );
};