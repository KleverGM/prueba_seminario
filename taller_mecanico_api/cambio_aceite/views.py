from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def revision_cambio_aceite(request):
    """
    Endpoint: POST /cambio-aceite/revision/
    Calcula kilómetros recorridos y determina si necesita cambio de aceite
    """
    try:
        km_actual = request.data.get('km_actual')
        km_ultimo_cambio = request.data.get('km_ultimo_cambio')
        
        # Validaciones
        if km_actual is None or km_ultimo_cambio is None:
            return Response({
                'mensaje': 'Error: debe proporcionar km_actual y km_ultimo_cambio'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            km_actual = float(km_actual)
            km_ultimo_cambio = float(km_ultimo_cambio)
        except (ValueError, TypeError):
            return Response({
                'mensaje': 'Error: km_actual y km_ultimo_cambio deben ser números válidos'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if km_actual < km_ultimo_cambio:
            return Response({
                'mensaje': 'Error: km_actual no puede ser menor que km_ultimo_cambio'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        # Calcular kilómetros recorridos
        km_recorridos = km_actual - km_ultimo_cambio
        
        # Determinar si necesita cambio según los condicionales
        if km_recorridos < 5000:
            mensaje = "No es necesario cambio inmediato"
        elif 5000 <= km_recorridos <= 8000:
            mensaje = "Recomendable programar cambio"
        else:  # km_recorridos > 8000
            mensaje = "Cambio urgente de aceite"
        
        return Response({
            'km_recorridos': km_recorridos,
            'mensaje': mensaje
        })
        
    except Exception as e:
        return Response({
            'mensaje': f'Error interno del servidor: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
