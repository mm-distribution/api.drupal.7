# DrupalGetRdfNamespacesTestCase::testGetRdfNamespaces()

- **Type:** Method
- **File:** [`modules/simpletest/tests/common.test`](../_file.md), lines 3169–3179 · [local source](../../../../../../source/modules/simpletest/tests/common.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test#L3169-L3179)
- **Class:** [DrupalGetRdfNamespacesTestCase](../DrupalGetRdfNamespacesTestCase.md)
- **Module/theme:** batch_test

## Signature

```php
function testGetRdfNamespaces()
```

## Documentation

```text
Test RDF namespaces.
```

## Code

```php
  function testGetRdfNamespaces() {
    // Fetches the front page and extracts XML namespaces.
    $this->drupalGet('');
    $xml = new SimpleXMLElement($this->content);
    $ns = $xml->getDocNamespaces();

    $this->assertEqual($ns['rdfs'], 'http://www.w3.org/2000/01/rdf-schema#', 'A prefix declared once is displayed.');
    $this->assertEqual($ns['foaf'], 'http://xmlns.com/foaf/0.1/', 'The same prefix declared in several implementations of hook_rdf_namespaces() is valid as long as all the namespaces are the same.');
    $this->assertEqual($ns['foaf1'], 'http://xmlns.com/foaf/0.1/', 'Two prefixes can be assigned the same namespace.');
    $this->assertTrue(!isset($ns['dc']), 'A prefix with conflicting namespaces is discarded.');
  }
```

---
_Drupal 7.103 · [modules/simpletest/tests/common.test](https://github.com/drupal/drupal/blob/7.103/modules/simpletest/tests/common.test) · Licensed GPL-2.0-or-later (see LICENSE)._
