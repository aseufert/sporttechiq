import wagtail.admin.rich_text.editors.draftail.features as draftail_features
from wagtail.admin.rich_text.converters.html_to_contentstate import BlockElementHandler
from wagtail.core import hooks
from collections import namedtuple


EditorPlugin = namedtuple('BlockPlugin', (
    'feature_name',
    'type',
    'tag',
    'control',
))


def _register_block_plugin(features, plugin):
    features.register_editor_plugin('draftail', plugin.feature_name, draftail_features.BlockFeature(plugin.control))
    features.register_converter_rule('contentstate', plugin.feature_name, {
        'from_database_format': {
            plugin.tag: BlockElementHandler(plugin.type),
        },
        'to_database_format': {
            'block_map': {
                plugin.type: plugin.tag,
            },
        },
    })


def _insert_feature_before(features, insert_feature, anchor_feature):
    try:
        index = features.default_features.index(anchor_feature)
    except ValueError:
        index = None
    if index is not None:
        features.default_features.insert(index, insert_feature)
    else:
        features.default_features.append(insert_feature)


@hooks.register('register_rich_text_features')
def register_center_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'center'
    type_ = 'paragraph-center'
    tag = 'p'

    control = {
        'type': type_,
        'label': 'Center',
        'description': 'p center',
        # Optionally, we can tell Draftail what element to use when displaying those blocks in the editor.
        'element': 'p',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )
    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'blockquote[class]': BlockElementHandler(type_)},
        'to_database_format': {
            'block_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'text-center',
                    },
                },
            },
        },
    })
    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_left_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'left'
    type_ = 'paragraph-left'
    tag = 'p'

    control = {
        'type': type_,
        'label': 'Left',
        'description': 'p left',
        'element': 'p',
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )
    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'blockquote[class]': BlockElementHandler(type_)},
        'to_database_format': {
            'block_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'text-left',
                    },
                },
            },
        },
    })
    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_right_feature(features):
    """
    Registering the `blockquote` feature, which uses the `blockquote` Draft.js block type,
    and is stored as HTML with a `<blockquote>` tag.
    """
    feature_name = 'right'
    type_ = 'paragraph-right'
    tag = 'p'

    control = {
        'type': type_,
        'label': 'Right',
        'description': 'p right',
        'element': 'p',
        'style': {'textDecoration': 'line-through'},
    }

    features.register_editor_plugin(
        'draftail', feature_name, draftail_features.BlockFeature(control)
    )
    features.register_converter_rule('contentstate', feature_name, {
        'from_database_format': {'blockquote[class]': BlockElementHandler(type_)},
        'to_database_format': {
            'block_map': {
                type_: {
                    'element': tag,
                    'props': {
                        'class': 'text-right',
                    },
                },
            },
        },
    })
    features.default_features.append(feature_name)


@hooks.register('register_rich_text_features')
def register_h1_feature(features):
    type_ = 'h1'
    tag = 'h1'
    plugin = EditorPlugin(
        feature_name=type_,
        type=type_,
        tag=tag,
        control={
            'type': type_,
            'label': 'H1',
            'description': 'Heading 1',
            'element': tag,
        })
    _register_block_plugin(features, plugin)
    _insert_feature_before(features, type_, 'h2')  # Insert h1 before h2
