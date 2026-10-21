# RdfTrackerAttributesTestCase::testAttributesInTracker()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 604–615 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L604-L615)
- **Class:** [RdfTrackerAttributesTestCase](../RdfTrackerAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testAttributesInTracker()
```

## Documentation

```text
Create nodes as both admin and anonymous user and test for correct RDFa
markup on the tracker page for those nodes and their comments.
```

## Code

```php
  function testAttributesInTracker() {
    // Create node as anonymous user.
    $node_anon = $this->drupalCreateNode(array('type' => 'article', 'uid' => 0));
    // Create node as admin user.
    $node_admin = $this->drupalCreateNode(array('type' => 'article', 'uid' => 1));

    // Pass both the anonymously posted node and the administrator posted node
    // through to test for the RDF attributes.
    $this->_testBasicTrackerRdfaMarkup($node_anon);
    $this->_testBasicTrackerRdfaMarkup($node_admin);

  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
