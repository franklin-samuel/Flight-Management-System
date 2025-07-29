import { useEffect, useState } from "react";
import { getVoos } from "../services/vooService";

export default function Voos() {
    const [voos, setVoos] = useState([])

    useEffect(() => {
        getVoos().then(setVoos)
    }, [])

    return (
        <div>
            <h1>Voos Disponíveis</h1>
            <ul>
                {voos.map((voo: any) => (
                    <li key={voo.numero_voo}>
                        {voo.origem} → {voo.destino} ({voo.capacidade} lugares)
                    </li>
                ))}
            </ul>
        </div>
    )
}
