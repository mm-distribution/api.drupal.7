# RdfMappingDefinitionTestCase::testAttributesInMarkup1()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 296–308 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L296-L308)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testAttributesInMarkup1()
```

## Documentation

```text
Create a node of type blog and test whether the RDF mapping defined for
this node type in rdf_test.module is used in the node page.
```

## Code

```php
  function testAttributesInMarkup1() {
    $node = $this->drupalCreateNode(array('type' => 'blog'));
    $isoDate = date('c', $node->changed);
    $url = url('node/' . $node->nid);
    $this->drupalGet('node/' . $node->nid);

    // Ensure the default bundle mapping for node is used. These attributes come
    // from the node default bundle definition.
    $blog_title = $this->xpath("//div[@about='$url']/span[@property='dc:title' and @content='$node->title']");
    $blog_meta = $this->xpath("//div[(@about='$url') and (@typeof='sioct:Weblog')]//span[contains(@property, 'dc:date') and contains(@property, 'dc:created') and @datatype='xsd:dateTime' and @content='$isoDate']");
    $this->assertTrue(!empty($blog_title), 'Property dc:title is present in meta tag.');
    $this->assertTrue(!empty($blog_meta), 'RDF type is present on post. Properties dc:date and dc:created are present on post date.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
