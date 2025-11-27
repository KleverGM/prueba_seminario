from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def calcular_costo_total(request):

    try:
        costos = request.data.get('costos', [])
        
        if not isinstance(costos, list):
            return Response({
                'mensaje': 'Error: el costo debe de ser un numero'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if not costos:
            return Response({
                'mensaje': 'Error: debe ingresar el costo'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        costos_numericos = []
        for costo in costos:
            try:
                costos_numericos.append(float(costo))
            except (ValueError, TypeError):
                return Response({
                    'mensaje': f'Error: {costo} no es un numero'
                }, status=status.HTTP_400_BAD_REQUEST)
        
        total = sum(costos_numericos)
        
        if total < 100:
            tipo_reparacion = "Reparacion economica"
        elif 100 <= total <= 500:
            tipo_reparacion = "Reparacion media"
        else: 
            tipo_reparacion = "Reparacion costosa"
        
        return Response({
            'total': total,
            'mensaje': f'Costo total calculado: ${total}. Clasificación: {tipo_reparacion}'
        })
        
    except Exception as e:
        return Response({
            'mensaje': f'Error interno del servidor: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)