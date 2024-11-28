import './Lists.css'
import React from 'react'
import axios from 'axios'

import { useEffect, useState } from 'react'
import { GoPlusCircle } from 'react-icons/go'
import ListItem from '../ListItem/ListItem'

const Lists = () => {
  const [data, setData] = useState([])
  const [erro, setError] = useState(null)
  const [loading, setLoading] = useState(true)

  useEffect(() => {
    axios
      .get('http://localhost:8000/api/listas/@eduarda?format=json')
      .then(response => {
        console.log('Raw Response:', response.data)
        setData(response.data)
        setLoading(false)
      })
      .catch(error => {
        setError(error)
        setLoading(false)
      })
  }, [])

  if (loading) return <div>Carregando ...</div>
  if (erro) return <div>Erro ao carregar os dados: {erro.message}</div>

  return (
    <div className="ListContent">
      <div className="info">
        <h2>Listas de Livros</h2>
        <GoPlusCircle id="add-icon" size={28} />
      </div>
      <div className="lists">
        {data.map((list, index) => (
          <ListItem
            key={index}
            listName={list.lista}
            numBooks={list.livros.length}
            description={'Sem descrição disponível'}
            books={list.livros}
          />
        ))}
      </div>
    </div>
  )
}

export default Lists
