# RdfMappingDefinitionTestCase::getInfo()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 280–286 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L280-L286)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public static function getInfo()
```

## Documentation

_No docblock in source._

## Code

```php
  public static function getInfo() {
    return array(
      'name' => 'RDF mapping definition functionality',
      'description' => 'Test the different types of RDF mappings and ensure the proper RDFa markup in included in nodes and user profile pages.',
      'group' => 'RDF',
    );
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
