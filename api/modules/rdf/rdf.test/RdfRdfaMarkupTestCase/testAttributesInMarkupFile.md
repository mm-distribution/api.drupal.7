# RdfRdfaMarkupTestCase::testAttributesInMarkupFile()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 121–208 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L121-L208)
- **Class:** [RdfRdfaMarkupTestCase](../RdfRdfaMarkupTestCase.md)
- **Module/theme:** rdf

## Signature

```php
function testAttributesInMarkupFile()
```

## Documentation

```text
Ensure that file fields have the correct resource as the object in RDFa
when displayed as a teaser.
```

## Code

```php
  function testAttributesInMarkupFile() {
    // Create a user to post the image.
    $admin_user = $this->drupalCreateUser(array('edit own article content', 'revert revisions', 'administer content types'));
    $this->drupalLogin($admin_user);

    $langcode = LANGUAGE_NONE;
    $bundle_name = "article";

    $field_name = 'file_test';
    $field = array(
      'field_name' => $field_name,
      'type' => 'file',
    );
    field_create_field($field);
    $instance = array(
      'field_name' => $field_name,
      'entity_type' => 'node',
      'bundle' => $bundle_name,
      'display' => array(
        'teaser' => array(
          'type' => 'file_default',
        ),
      ),
    );
    field_create_instance($instance);

    // Set the RDF mapping for the new field.
    $rdf_mapping = rdf_mapping_load('node', $bundle_name);
    $rdf_mapping += array($field_name => array('predicates' => array('rdfs:seeAlso'), 'type' => 'rel'));
    $rdf_mapping_save = array('mapping' => $rdf_mapping, 'type' => 'node', 'bundle' => $bundle_name);
    rdf_mapping_save($rdf_mapping_save);

    // Get the test file that simpletest provides.
    $file = current($this->drupalGetTestFiles('text'));

    // Prepare image variables.
    $image_field = "field_image";
    // Get the test image that simpletest provides.
    $image = current($this->drupalGetTestFiles('image'));

    // Create an array for drupalPost with the field names as the keys and
    // the URIs for the test files as the values.
    $edit = array("files[" . $field_name . "_" . $langcode . "_0]" => drupal_realpath($file->uri),
                  "files[" . $image_field . "_" . $langcode . "_0]" => drupal_realpath($image->uri));

    // Create node and save, then edit node to upload files.
    $node = $this->drupalCreateNode(array('type' => 'article', 'promote' => 1));
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));

    // Get filenames and nid for comparison with HTML output.
    $file_filename = $file->filename;
    $image_filename = $image->filename;
    $nid = $node->nid;
    // Navigate to front page, where node is displayed in teaser form.
    $this->drupalGet('node');

    // We only check to make sure that the resource attribute contains '.txt'
    // instead of the full file name because the filename is altered on upload.
    $file_rel = $this->xpath('//div[contains(@about, :node-uri)]//div[contains(@rel, "rdfs:seeAlso") and contains(@resource, ".txt")]', array(
      ':node-uri' => 'node/' . $nid,
    ));
    $this->assertTrue(!empty($file_rel), "Attribute 'rel' set on file field. Attribute 'resource' is also set.");
    $image_rel = $this->xpath('//div[contains(@about, :node-uri)]//div[contains(@rel, "rdfs:seeAlso") and contains(@resource, :image)]//img[contains(@typeof, "foaf:Image")]', array(
      ':node-uri' => 'node/' . $nid,
      ':image' => $image_filename,
    ));

    $this->assertTrue(!empty($image_rel), "Attribute 'rel' set on image field. Attribute 'resource' is also set.");

    // Edits the node to add tags.
    $tag1 = $this->randomName(8);
    $tag2 = $this->randomName(8);
    $edit = array();
    $edit['field_tags[' . LANGUAGE_NONE . ']'] = "$tag1, $tag2";
    $this->drupalPost('node/' . $node->nid . '/edit', $edit, t('Save'));
    // Ensures the RDFa markup for the relationship between the node and its
    // tags is correct.
    $term_rdfa_meta = $this->xpath('//div[@about=:node-url and contains(@typeof, "sioc:Item") and contains(@typeof, "foaf:Document")]//ul[@class="links"]/li[@rel="dc:subject"]/a[@typeof="skos:Concept" and @datatype="" and text()=:term-name]', array(
      ':node-url' => url('node/' . $node->nid),
      ':term-name' => $tag1,
    ));
    $this->assertTrue(!empty($term_rdfa_meta), 'Property dc:subject is present for the tag1 field item.');
    $term_rdfa_meta = $this->xpath('//div[@about=:node-url and contains(@typeof, "sioc:Item") and contains(@typeof, "foaf:Document")]//ul[@class="links"]/li[@rel="dc:subject"]/a[@typeof="skos:Concept" and @datatype="" and text()=:term-name]', array(
      ':node-url' => url('node/' . $node->nid),
      ':term-name' => $tag2,
    ));
    $this->assertTrue(!empty($term_rdfa_meta), 'Property dc:subject is present for the tag2 field item.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
