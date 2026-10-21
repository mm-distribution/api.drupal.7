# RdfCommentAttributesTestCase::testNumberOfCommentsRdfaMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 458–474 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L458-L474)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public function testNumberOfCommentsRdfaMarkup()
```

## Documentation

```text
Tests the presence of the RDFa markup for the number of comments.
```

## Code

```php
  public function testNumberOfCommentsRdfaMarkup() {
    // Posts 2 comments as a registered user.
    $this->drupalLogin($this->web_user);
    $this->postComment($this->node1, $this->randomName(), $this->randomName());
    $this->postComment($this->node1, $this->randomName(), $this->randomName());

    // Tests number of comments in teaser view.
    $this->drupalGet('node');
    $node_url = url('node/' . $this->node1->nid);
    $comment_count_teaser = $this->xpath('//div[@about=:node-url]/span[@property="sioc:num_replies" and @content="2" and @datatype="xsd:integer"]', array(':node-url' => $node_url));
    $this->assertTrue(!empty($comment_count_teaser), 'RDFa markup for the number of comments found on teaser view.');

    // Tests number of comments in full node view.
    $this->drupalGet('node/' . $this->node1->nid);
    $comment_count_teaser = $this->xpath('//div[@about=:node-url]/span[@property="sioc:num_replies" and @content="2" and @datatype="xsd:integer"]', array(':node-url' => $node_url));
    $this->assertTrue(!empty($comment_count_teaser), 'RDFa markup for the number of comments found on full node view.');
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
