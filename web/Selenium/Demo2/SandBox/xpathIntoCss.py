
вуа xPathToCss(xpath):

        xpath1 = xpath.replace(/\[(\d+?)\]/g, function(s,m1){ return '['+(m1-1)+']'; })
        xpath2 = xpath1.replace(/\/{2}/g, '')
        xpath3 = xpath2.replace(/\/+/g, ' > ')
        xpath4 = xpath3.replace(/@/g, '')
        xpath5 = xpath4.replace(/\[(\d+)\]/g, ':eq($1)')
        .replace(/^\s+/, '');

    return xpath
