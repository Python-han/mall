from rest_framework import renderers


class JSONRenderer(renderers.JSONRenderer):
    
    def render(self, data, accepted_media_type=None, renderer_context=None):
        if renderer_context:
            data['code'] = renderer_context['response'].status_code
            data['message'] = renderer_context['response'].status_text
        return super().render(data, accepted_media_type, renderer_context)