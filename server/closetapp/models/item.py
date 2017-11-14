from database import db
from sqlalchemy.types import Enum, String, Integer, Boolean, DateTime

class Item(db.Model):
	__tablename__ = 'items'
	id = db.Column(Integer, primary_key=True)
	color = db.Column(Enum('white','Black','Orange','Yellow','Yellow_Green','Green','Blue Green','Blue','Blue_Violet','Violet','Mauve','Mauve_Pink','Pink','Red'))
	color_code = db.Column(Enum('very light','light','medium','strong','very strong'))
	color_solid = db.Column(Boolean)
	loose_tight = db.Column(Enum('loose','mid','tight'))
	texture = db.Column(Enum('cotton','leather','denim','silk','knit','woolen','fur_leather','mixed','polyster','stiff_satin'))
	bottom_top = db.Column(Enum('bottom','top','all'))
	category = db.Column(Enum('t-shirt','short_sleeve','short_skirt','long_skirt','jeans','pants','shorts','shirt','blouse','jacket','knits','sweater','tank-top','cardigan','long_jacket','long_sweater','dress','jump_suit','sports_long_sleeve'))
	warmth_level = db.Column(Enum('1','2','3'))
	image_url = db.Column(String(100))
	created_at = db.Column(DateTime)
	updated_at = db.Column(DateTime)

	@property
	def serialize(self):
		return {
			'id': self.id,
			'color': self.color,
			'color_code': self.color_code,
			'color_solid': self.color_solid,
			'loose_tight': self.loose_tight,
			'texture': self.texture,
			'bottom_top': self.bottom_top,
			'category': self.category,
			'warmth_level': self.warmth_level,
			'image_url': self.image_url,
			'created_at': self.created_at,
			'updated_at': self.updated_at
		}
