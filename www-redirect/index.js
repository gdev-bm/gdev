export default {
  fetch(request) {
    const url = new URL(request.url);
    url.hostname = 'gdev.bm';
    return Response.redirect(url.toString(), 301);
  },
};
