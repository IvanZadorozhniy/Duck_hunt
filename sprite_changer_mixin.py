class SpriteChangerMixin():
    def _change_animation(self, next_animation):
        self.animation.stop()
        next_animation.scale(self.size)
        self.animation = next_animation
        self.animation.play()