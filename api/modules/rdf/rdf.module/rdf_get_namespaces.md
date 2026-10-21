# rdf_get_namespaces()

- **Type:** Function
- **File:** [`modules/rdf/rdf.module`](_file.md), lines 97–119 · [local source](../../../../source/modules/rdf/rdf.module) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module#L97-L119)
- **Module/theme:** rdf
- **Topics:** [rdf](../../../topics/rdf.md)

## Signature

```php
function rdf_get_namespaces()
```

## Documentation

```text
Returns an array of RDF namespaces defined in modules that implement
hook_rdf_namespaces().
```

## Code

```php
function rdf_get_namespaces() {
  $rdf_namespaces = module_invoke_all('rdf_namespaces');
  // module_invoke_all() uses array_merge_recursive() which might return nested
  // arrays if several modules redefine the same prefix multiple times. We need
  // to ensure the array of namespaces is flat and only contains strings as
  // URIs.
  foreach ($rdf_namespaces as $prefix => $uri) {
    if (is_array($uri)) {
      if (count(array_unique($uri)) == 1) {
        // All namespaces declared for this prefix are the same, merge them all
        // into a single namespace.
        $rdf_namespaces[$prefix] = $uri[0];
      }
      else {
        // There are conflicting namespaces for this prefix, do not include
        // duplicates in order to avoid asserting any inaccurate RDF
        // statements.
        unset($rdf_namespaces[$prefix]);
      }
    }
  }
  return $rdf_namespaces;
}
```

---
_Drupal 7.103 · [modules/rdf/rdf.module](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.module) · Licensed GPL-2.0-or-later (see LICENSE)._
