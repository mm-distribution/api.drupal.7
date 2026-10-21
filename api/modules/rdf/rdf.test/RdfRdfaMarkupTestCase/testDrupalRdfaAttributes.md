# RdfRdfaMarkupTestCase::testDrupalRdfaAttributes()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 60–115 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L60-L115)
- **Class:** [RdfRdfaMarkupTestCase](../RdfRdfaMarkupTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testDrupalRdfaAttributes()
```

## Documentation

```text
Test rdf_rdfa_attributes().
```

## Code

```php
  function testDrupalRdfaAttributes() {
    // Same value as the one in the HTML tag (no callback function).
    $expected_attributes = array(
      'property' => array('dc:title'),
    );
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $attributes = rdf_rdfa_attributes($mapping['title']);
    ksort($expected_attributes);
    ksort($attributes);
    $this->assertEqual($expected_attributes, $attributes);

    // Value different from the one in the HTML tag (callback function).
    $date = 1252750327;
    $isoDate = date('c', $date);
    $expected_attributes = array(
      'datatype' => 'xsd:dateTime',
      'property' => array('dc:created'),
      'content' => $isoDate,
    );
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $attributes = rdf_rdfa_attributes($mapping['created'], $date);
    ksort($expected_attributes);
    ksort($attributes);
    $this->assertEqual($expected_attributes, $attributes);

    // Same value as the one in the HTML tag with datatype.
    $expected_attributes = array(
      'datatype' => 'foo:bar1type',
      'property' => array('foo:bar1'),
    );
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $attributes = rdf_rdfa_attributes($mapping['foobar1']);
    ksort($expected_attributes);
    ksort($attributes);
    $this->assertEqual($expected_attributes, $attributes);

    // ObjectProperty mapping (rel).
    $expected_attributes = array(
      'rel' => array('sioc:has_creator', 'dc:creator'),
    );
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $attributes = rdf_rdfa_attributes($mapping['foobar_objproperty1']);
    ksort($expected_attributes);
    ksort($attributes);
    $this->assertEqual($expected_attributes, $attributes);

    // Inverse ObjectProperty mapping (rev).
    $expected_attributes = array(
      'rev' => array('sioc:reply_of'),
    );
    $mapping = rdf_mapping_load('test_entity', 'test_bundle');
    $attributes = rdf_rdfa_attributes($mapping['foobar_objproperty2']);
    ksort($expected_attributes);
    ksort($attributes);
    $this->assertEqual($expected_attributes, $attributes);
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
