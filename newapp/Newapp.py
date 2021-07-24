@api_view(['GET', 'POST', 'DELETE'])
def newapp_list(request):
    ...

    elif request.method == 'POST':
    newapps_data = JSONParser().parse(request)
    newapps_serializer = TutorialSerializer(data=tutorial_data)
    if newapps_serializer.is_valid():
        newapps_serializer.save()
        return JsonResponse(tutorial_serializer.data, status=status.HTTP_201_CREATED)
    return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST', 'DELETE'])
def newapp_list(request):
    if request.method == 'GET':
        newapps = Tutorial.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            newapp = tutorials.filter(title__icontains=title)

        newapp_serializer = NewappSerializer(tutorials, many=True)
        return JsonResponse(newapp_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    @api_view(['GET', 'PUT', 'DELETE'])
    def newapps_detail(request, pk):
        # ... tutorial = Tutorial.objects.get(pk=pk)

        if request.method == 'GET':
            newapp_serializer = newapp_serializer(tutorial)
            return JsonResponse(newapp_serializer.data)

        @api_view(['GET', 'PUT', 'DELETE'])
        def newapp_detail(request, pk):
            # ... tutorial = Tutorial.objects.get(pk=pk)
            # ...

            elif request.method == 'PUT':
            newapps_data = JSONParser().parse(request)
            newapps_serializer = newappSerializer(tutorial, data=tutorial_data)
            if newapps_serializer.is_valid():
                newapps_serializer.save()
                return JsonResponse(newapps_serializer.data)
            return JsonResponse(newapps_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        @api_view(['GET', 'PUT', 'DELETE'])
        def newapp_detail(request, pk):
            # ... tutorial = Tutorial.objects.get(pk=pk)
            # ...

            elif request.method == 'DELETE':
            newapps.delete()
            return JsonResponse({'message': 'Tutorial was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

        @api_view(['GET', 'POST', 'DELETE'])
        def newapps_list(request):
            # ...

            elif request.method == 'DELETE':
            count = newapps.objects.all().delete()
            return JsonResponse({'message': '{} newapp were deleted successfully!'.format(count[0])},
                                status=status.HTTP_204_NO_CONTENT)

        @api_view(['GET'])
        def newapps_list_published(request):
            tutorials = newapps.objects.filter(published=True)

            if request.method == 'GET':
                newapps_serializer = newappSerializer(tutorials, many=True)
                return JsonResponse(newapps_serializer.data, safe=False)