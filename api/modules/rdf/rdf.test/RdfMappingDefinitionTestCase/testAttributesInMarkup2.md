# RdfMappingDefinitionTestCase::testAttributesInMarkup2()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 314–331 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L314-L331)
- **Class:** [RdfMappingDefinitionTestCase](../RdfMappingDefinitionTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testAttributesInMarkup2()
```

## Documentation

```text
Create a content type and a node of type test_bundle_hook_install and test
whether the RDF mapping defined in rdf_test.install is used.
```

## Code

```php
  function testAttributesInMarkup2() {
    $type = $this->drupalCreateContentType(array('type' => 'test_bundle_hook_install'));
    // Create node with single quotation mark title to ensure it does not get
    // escaped more than once.
    $node = $this->drupalCreateNode(array(
      'type' => 'test_bundle_hook_install',
      'title' => $this->randomName(8) . "'",
    ));
    $isoDate = date('c', $node->changed);
    $url = url('node/' . $node->nid);
    $this->drupalGet('node/' . $node->nid);

    // Ensure the mapping defined in rdf_module.test is used.
    $test_bundle_title = $this->xpath("//div[@about='$url']/span[@property='dc:title' and @content=\"$node->title\"]");
    $test_bundle_meta = $this->xpath("//div[(@about='$url') and contains(@typeof, 'foo:mapping_install1') and contains(@typeof, 'bar:mapping_install2')]//span[contains(@property, 'dc:date') and contains(@property, 'dc:created') and @datatype='xsd:dateTime' and @content='$isoDate']");
    $this->assertTrue(!empty($test_bundle_title), 'Property dc:title is present in meta tag.');
    $this->assertTrue(!empty($test_bundle_meta), 'RDF type is present on post. Properties dc:date and dc:created are present on post date.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
