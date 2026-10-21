# RdfGetRdfNamespacesTestCase::testGetRdfNamespaces()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 711–719 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L711-L719)
- **Class:** [RdfGetRdfNamespacesTestCase](../RdfGetRdfNamespacesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testGetRdfNamespaces()
```

## Documentation

```text
Test getting RDF namesapces.
```

## Code

```php
  function testGetRdfNamespaces() {
    // Get all RDF namespaces.
    $ns = rdf_get_namespaces();

    $this->assertEqual($ns['rdfs'], 'http://www.w3.org/2000/01/rdf-schema#', 'A prefix declared once is included.');
    $this->assertEqual($ns['foaf'], 'http://xmlns.com/foaf/0.1/', 'The same prefix declared in several implementations of hook_rdf_namespaces() is valid as long as all the namespaces are the same.');
    $this->assertEqual($ns['foaf1'], 'http://xmlns.com/foaf/0.1/', 'Two prefixes can be assigned the same namespace.');
    $this->assertTrue(!isset($ns['dc']), 'A prefix with conflicting namespaces is discarded.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
