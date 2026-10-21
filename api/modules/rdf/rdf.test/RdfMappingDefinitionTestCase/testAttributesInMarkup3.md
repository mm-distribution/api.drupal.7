# RdfMappingDefinitionTestCase::testAttributesInMarkup3()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 337–350 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L337-L350)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testAttributesInMarkup3()
```

## Documentation

```text
Create a random content type and node and ensure the default mapping for
node is used.
```

## Code

```php
  function testAttributesInMarkup3() {
    $type = $this->drupalCreateContentType();
    $node = $this->drupalCreateNode(array('type' => $type->type));
    $isoDate = date('c', $node->changed);
    $url = url('node/' . $node->nid);
    $this->drupalGet('node/' . $node->nid);

    // Ensure the default bundle mapping for node is used. These attributes come
    // from the node default bundle definition.
    $random_bundle_title = $this->xpath("//div[@about='$url']/span[@property='dc:title' and @content='$node->title']");
    $random_bundle_meta = $this->xpath("//div[(@about='$url') and contains(@typeof, 'sioc:Item') and contains(@typeof, 'foaf:Document')]//span[contains(@property, 'dc:date') and contains(@property, 'dc:created') and @datatype='xsd:dateTime' and @content='$isoDate']");
    $this->assertTrue(!empty($random_bundle_title), 'Property dc:title is present in meta tag.');
    $this->assertTrue(!empty($random_bundle_meta), 'RDF type is present on post. Properties dc:date and dc:created are present on post date.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
