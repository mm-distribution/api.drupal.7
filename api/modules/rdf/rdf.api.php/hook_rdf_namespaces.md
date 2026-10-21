# hook_rdf_namespaces()

- **Type:** Hook (documentation function)
- **File:** [`modules/rdf/rdf.api.php`](_file.md), lines 90–102 · [local source](../../../../source/modules/rdf/rdf.api.php) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.api.php#L90-L102)
- **Module/theme:** rdf
- **Topics:** [hooks](../../../topics/hooks.md), [rdf](../../../topics/rdf.md)

## Signature

```php
function hook_rdf_namespaces()
```

## Documentation

```text
Allow modules to define namespaces for RDF mappings.

Many common namespace prefixes are defined in rdf_rdf_namespaces(). However,
if a module implements hook_rdf_mapping() and uses a prefix that is not
defined in rdf_rdf_namespaces(), this hook should be used to define the new
namespace prefix.

@return
  An associative array of namespaces where the key is the namespace prefix
  and the value is the namespace URI.

@ingroup rdf
```

## Code

```php
function hook_rdf_namespaces() {
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

## Implementations in Drupal core (derived)

Functions whose docblock says "Implements hook_rdf_namespaces()".

- [rdf_rdf_namespaces()](../rdf.module/rdf_rdf_namespaces.md) — `modules/rdf/rdf.module`
- [rdf_test_rdf_namespaces()](../tests/rdf_test.module/rdf_test_rdf_namespaces.md) — `modules/rdf/tests/rdf_test.module`

---
_Drupal 7.103 · [modules/rdf/rdf.api.php](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.api.php) · Licensed GPL-2.0-or-later (see LICENSE)._
