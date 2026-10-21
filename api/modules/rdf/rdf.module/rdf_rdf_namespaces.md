# rdf_rdf_namespaces()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 79–91 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L79-L91)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)
- **Implements:** [hook_rdf_namespaces()](../rdf.api.php/hook_rdf_namespaces.md)

## Signature

```php
function rdf_rdf_namespaces()
```

## Documentation

```text
Implements hook_rdf_namespaces().
```

## Code

```php
function rdf_rdf_namespaces() {
  return array(
    'content'  => 'http://purl.org/rss/1.0/modules/content/',
    'dc'       => 'http://purl.org/dc/terms/',
    'foaf'     => 'http://xmlns.com/foaf/0.1/',
    'og'       => 'http://ogp.me/ns#',
    'rdfs'     => 'http://www.w3.org/2000/01/rdf-schema#',
    'sioc'     => 'http://rdfs.org/sioc/ns#',
    'sioct'    => 'http://rdfs.org/sioc/types#',
    'skos'     => 'http://www.w3.org/2004/02/skos/core#',
    'xsd'      => 'http://www.w3.org/2001/XMLSchema#',
  );
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
