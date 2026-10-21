# RdfCommentAttributesTestCase::testCommentReplyOfRdfaMarkup()

- **Type:** Method
- **File:** [`modules/rdf/rdf.test`](../_file.md), lines 531–552 · [local source](../../../../../source/modules/rdf/rdf.test) · [GitHub](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test#L531-L552)
- **Class:** [RdfCommentAttributesTestCase](../RdfCommentAttributesTestCase.md)
- **Module/theme:** rdf

## Signature

```php
public function testCommentReplyOfRdfaMarkup()
```

## Documentation

```text
Test RDF comment replies.
```

## Code

```php
  public function testCommentReplyOfRdfaMarkup() {
    // Posts comment #1 as a registered user.
    $this->drupalLogin($this->web_user);
    $comments[] = $this->postComment($this->node1, $this->randomName(), $this->randomName());

    // Tests the reply_of relationship of a first level comment.
    $result = $this->xpath("(id('comments')//div[contains(@class,'comment ')])[position()=1]//span[@rel='sioc:reply_of' and @resource=:node]", array(':node' => url("node/{$this->node1->nid}")));
    $this->assertEqual(1, count($result), 'RDFa markup referring to the node is present.');
    $result = $this->xpath("(id('comments')//div[contains(@class,'comment ')])[position()=1]//span[@rel='sioc:reply_of' and @resource=:comment]", array(':comment' => url('comment/1#comment-1')));
    $this->assertFalse($result, 'No RDFa markup referring to the comment itself is present.');

    // Posts a reply to the first comment.
    $this->drupalGet('comment/reply/' . $this->node1->nid . '/' . $comments[0]->id);
    $comments[] = $this->postComment(NULL, $this->randomName(), $this->randomName(), TRUE);

    // Tests the reply_of relationship of a second level comment.
    $result = $this->xpath("(id('comments')//div[contains(@class,'comment ')])[position()=2]//span[@rel='sioc:reply_of' and @resource=:node]", array(':node' => url("node/{$this->node1->nid}")));
    $this->assertEqual(1, count($result), 'RDFa markup referring to the node is present.');
    $result = $this->xpath("(id('comments')//div[contains(@class,'comment ')])[position()=2]//span[@rel='sioc:reply_of' and @resource=:comment]", array(':comment' => url('comment/1', array('fragment' => 'comment-1'))));
    $this->assertEqual(1, count($result), 'RDFa markup referring to the parent comment is present.');
    $comments = $this->xpath("(id('comments')//div[contains(@class,'comment ')])[position()=2]");
  }
```

---
_Drupal 7.103 · [modules/rdf/rdf.test](https://github.com/drupal/drupal/blob/7.103/modules/rdf/rdf.test) · Licensed GPL-2.0-or-later (see LICENSE)._
