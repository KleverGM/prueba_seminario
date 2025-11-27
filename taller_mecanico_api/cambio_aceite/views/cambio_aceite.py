from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def revision_cambio_aceite(request):
   
    try:
        km_actual = request.data.get('km_actual')
        km_ultimo_cambio = request.data.get('km_ultimo_cambio')
        
        if km_actual is None or km_ultimo_cambio is None:
            return Response({
                'mensaje': 'Error: debe proporcionar el km actual y el ultimo cambio'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            km_actual = float(km_actual)
            km_ultimo_cambio = float(km_ultimo_cambio)
        except (ValueError, TypeError):
            return Response({
                'mensaje': 'Error: el km actual y el ultimo cambio deben ser numeros validos'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        if km_actual < km_ultimo_cambio:
            return Response({
                'mensaje': 'Error: el km actual no puede ser menor que el ultimo cambio'
            }, status=status.HTTP_400_BAD_REQUEST)
        
        km_recorridos = km_actual - km_ultimo_cambio
        
        if km_recorridos < 5000:
            mensaje = "No es necesario un cambio inmediato de aceite"
        elif 5000 <= km_recorridos <= 8000:
            mensaje = "Recomendable realizar un cambio de aceite"
        else:
            mensaje = "Realizar un cambio urgente de aceite"
        
        return Response({
            'km_recorridos': km_recorridos,
            'mensaje': mensaje
        })
        
    except Exception as e:
        return Response({
            'mensaje': f'Error interno del servidor: {str(e)}'
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)