# file_create_url()

- **Type:** Function
- **File:** [`includes/file.inc`](_file.md), lines 381–419 · [local source](../../../source/includes/file.inc) · [GitHub](https://github.com/drupal/drupal/blob/7.103/includes/file.inc#L381-L419)
- **Topics:** [file](../../topics/file.md)

## Signature

```php
function file_create_url($uri)
```

## Documentation

```text
Creates a web-accessible URL for a stream to an external or local file.

Compatibility: normal paths and stream wrappers.

There are two kinds of local files:
- "managed files", i.e. those stored by a Drupal-compatible stream wrapper.
  These are files that have either been uploaded by users or were generated
  automatically (for example through CSS aggregation).
- "shipped files", i.e. those outside of the files directory, which ship as
  part of Drupal core or contributed modules or themes.

@param $uri
  The URI to a file for which we need an external URL, or the path to a
  shipped file.

@return
  A string containing a URL that may be used to access the file.
  If the provided string already contains a preceding 'http', 'https', or
  '/', nothing is done and the same string is returned. If a stream wrapper
  could not be found to generate an external URL, then FALSE is returned.

@see http://drupal.org/node/515192
```

## Code

```php
function file_create_url($uri) {
  // Allow the URI to be altered, e.g. to serve a file from a CDN or static
  // file server.
  drupal_alter('file_url', $uri);

  $scheme = file_uri_scheme($uri);

  if (!$scheme) {
    // Allow for:
    // - root-relative URIs (e.g. /foo.jpg in http://example.com/foo.jpg)
    // - protocol-relative URIs (e.g. //bar.jpg, which is expanded to
    //   http://example.com/bar.jpg by the browser when viewing a page over
    //   HTTP and to https://example.com/bar.jpg when viewing a HTTPS page)
    // Both types of relative URIs are characterized by a leading slash, hence
    // we can use a single check.
    if (drupal_substr($uri, 0, 1) == '/') {
      return $uri;
    }
    else {
      // If this is not a properly formatted stream, then it is a shipped file.
      // Therefore, return the urlencoded URI with the base URL prepended.
      return $GLOBALS['base_url'] . '/' . drupal_encode_path($uri);
    }
  }
  elseif ($scheme == 'http' || $scheme == 'https') {
    // Check for HTTP so that we don't have to implement getExternalUrl() for
    // the HTTP wrapper.
    return $uri;
  }
  else {
    // Attempt to return an external URL using the appropriate wrapper.
    if ($wrapper = file_stream_wrapper_get_instance_by_uri($uri)) {
      return $wrapper->getExternalUrl();
    }
    else {
      return FALSE;
    }
  }
}
```

---
_Drupal 7.103 · [includes/file.inc](https://github.com/drupal/drupal/blob/7.103/includes/file.inc) · Licensed GPL-2.0-or-later (see LICENSE)._
